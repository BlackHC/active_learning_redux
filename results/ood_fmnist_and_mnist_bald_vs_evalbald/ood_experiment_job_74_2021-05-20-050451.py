store = {}
store['timestamp']=1621483491
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=74']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=74
store['worker_id']=74
store['num_workers']=80
store['config']={'seed': 1312, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.283432960510254})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.652592420578003})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2498421669006348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.041736602783203})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.974294662475586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.120570182800293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9288814067840576})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.373262405395508})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0897560119628906})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.180196762084961})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.7523728515625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 15798], ['id', 40457], ['id', 47651], ['id', 29464], ['id', 47322]], 'labels': [0, 0, 3, 3, 8], 'scores': [1.3654168459558242, 2.4084689467125155, 3.248377653940781, 3.822464973800198, 4.175733903506703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2285923957824707})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6419267654418945})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.6744585037231445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.527541160583496})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6876, 'crossentropy': 1.9454990234375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 19298], ['id', 36321], ['id', 32512], ['id', 2247], ['id', 1213]], 'labels': [6, 2, 4, 9, 2], 'scores': [1.0676457914028838, 2.003026891996669, 2.835800150144335, 3.438611410682589, 3.8523069735803626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7195106744766235})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0459797382354736})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.18203067779541})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.3188042640686035})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.5099613666534424})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.4792826175689697})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.549886703491211})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.4281539916992188})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.505244255065918})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7228, 'crossentropy': 2.13744375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 52896], ['id', 57150], ['id', 25747], ['id', 2246], ['id', 47081]], 'labels': [5, 7, 5, 7, 5], 'scores': [1.2768996565902946, 2.3931928553020443, 3.25116073155805, 3.821795057866659, 4.170137154528243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.797905683517456})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.1036548614501953})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.2694549560546875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3899435997009277})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.682868003845215})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.775294303894043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4977869987487793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.530829906463623})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.717822551727295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.8185064792633057})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.8539092540740967})
store['active_learning_steps'][3]['training']['best_epoch']=8
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 2.4626314453125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 46492], ['id', 4800], ['id', 31847], ['id', 1851], ['id', 38623]], 'labels': [9, 6, 8, 7, 8], 'scores': [1.2585731442180481, 2.3746526664138594, 3.251874794099564, 3.8435167185363532, 4.195193817043078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1730735301971436})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2774169445037842})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4486079216003418})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.7083631753921509})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.5919008255004883})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8127, 'crossentropy': 1.2104498046875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20388], ['id', 19149], ['id', 3795], ['id', 37089], ['id', 10210]], 'labels': [0, 2, 7, 5, 3], 'scores': [1.2315370148896165, 2.246367689419625, 3.0490271313255324, 3.6477608592520845, 4.027620183071155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.150252103805542})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3165924549102783})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.505515217781067})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.6943817138671875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6599464416503906})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7821, 'crossentropy': 1.31185791015625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17756], ['id', 21148], ['id', 21421], ['id', 5175], ['id', 22517]], 'labels': [8, 7, 8, 4, 5], 'scores': [1.1261427685127599, 2.155049380835056, 2.9797161824445784, 3.5586891859534306, 3.948537825883708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.160527229309082})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.4199621677398682})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.518973469734192})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6296823024749756})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.657752513885498})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.699453353881836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.7001686096191406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.7752416133880615})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8108, 'crossentropy': 1.54494501953125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 14271], ['id', 50449], ['id', 30400], ['id', 59314], ['id', 8847]], 'labels': [1, 2, 3, 9, 9], 'scores': [1.204233759648966, 2.30318253462241, 3.202851250829429, 3.7995905222059534, 4.172076287341065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0890133380889893})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.3196388483047485})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3475698232650757})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4039700031280518})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8056, 'crossentropy': 1.0068279296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20035], ['id', 29453], ['id', 33358], ['id', 32427], ['id', 35344]], 'labels': [8, 2, 9, 0, 2], 'scores': [0.9598393638384835, 1.8156282575414044, 2.541447630898869, 3.1126091420756943, 3.5586954598866596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2102242708206177})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2093863487243652})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1822357177734375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3193167448043823})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.410853385925293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3087878227233887})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3767883777618408})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5485360622406006})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.606017827987671})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8228, 'crossentropy': 1.3938826171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 50471], ['id', 11600], ['id', 4955], ['id', 17755], ['id', 10481]], 'labels': [4, 2, 2, 0, 6], 'scores': [1.2935809675482224, 2.4106013747962156, 3.2898465114306594, 3.8641547080971357, 4.200570303367153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9446737766265869})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9005595445632935})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.198693037033081})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1629159450531006})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3153066635131836})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8655, 'crossentropy': 0.83108720703125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 50806], ['id', 58471], ['id', 44625], ['id', 1812], ['id', 58560]], 'labels': [9, 5, 5, 4, 0], 'scores': [1.0352510197625875, 1.945097874397704, 2.7450074231576433, 3.3427049145427423, 3.7929116511847685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9792448282241821})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9957172274589539})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0636347532272339})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1202222108840942})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2962729930877686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1700592041015625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2019917964935303})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.4360740184783936})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2754956483840942})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8653, 'crossentropy': 0.97700087890625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 53872], ['id', 8033], ['id', 18150], ['id', 6089], ['id', 22747]], 'labels': [8, 8, 8, 3, 4], 'scores': [1.162075050436675, 2.2513061538004493, 3.118083950425973, 3.7524405227335125, 4.1294854618828225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.970748782157898})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.859992504119873})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9705803394317627})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9887406826019287})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0424962043762207})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.172034502029419})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9764053821563721})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9522855281829834})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8772, 'crossentropy': 0.9068400390625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 9948], ['id', 53156], ['id', 49537], ['id', 38256], ['id', 55834]], 'labels': [8, 3, 2, 2, 9], 'scores': [1.1560987919623442, 2.2162509890994206, 3.076331341154593, 3.7079573519355504, 4.111593714653848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9097504615783691})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9830158948898315})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9055993556976318})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9408300518989563})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9083008766174316})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0060014724731445})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0684564113616943})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1352438926696777})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8824, 'crossentropy': 0.86243291015625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 36417], ['id', 50320], ['id', 33812], ['id', 59468], ['id', 44706]], 'labels': [6, 5, 6, 7, 5], 'scores': [1.2037119772846396, 2.266787060737995, 3.1537292215458272, 3.793000318279983, 4.155184935351667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9283449649810791})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7983472347259521})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7602252960205078})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.925948441028595})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8622205257415771})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.973752498626709})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.649372900390625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 32504], ['id', 59280], ['id', 57728], ['id', 26412], ['id', 14540]], 'labels': [9, 8, 9, 3, 7], 'scores': [0.9706111224147655, 1.8787795389181232, 2.67655995908337, 3.3029439862043777, 3.7486071164579933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9697116613388062})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8079971075057983})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7934686541557312})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9026002883911133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9340895414352417})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9098577499389648})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9813616275787354})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0859243869781494})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9234910011291504})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.787204736328125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37352], ['id', 41959], ['id', 31301], ['id', 17494], ['id', 24311]], 'labels': [9, 1, 5, 5, 8], 'scores': [1.194277181352093, 2.2501123771124334, 3.07569451066101, 3.6928244364830842, 4.090527303355521]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8696780204772949})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7496734857559204})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7451035976409912})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.947490930557251})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9161998629570007})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8354778289794922})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1030280590057373})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.00972318649292})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1205308437347412})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.78504267578125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 1561], ['id', 57523], ['id', 27316], ['id', 21956], ['id', 17010]], 'labels': [2, 3, 3, 5, 3], 'scores': [1.3093601762970704, 2.4092693763317246, 3.2673955886767274, 3.8259282398207937, 4.167990382435312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.913654088973999})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7762826681137085})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8735496997833252})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9130819439888})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0041874647140503})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.70599970703125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 23472], ['id', 43043], ['id', 46953], ['id', 23104], ['id', 2381]], 'labels': [2, 3, 3, 0, 7], 'scores': [0.9427763002053622, 1.762987268639944, 2.4773718725514717, 3.0646054768887154, 3.5272846167225875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8194318413734436})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7923182845115662})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8136684894561768})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.040264368057251})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9147406220436096})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8445475101470947})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7865716814994812})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9169108867645264})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8328534364700317})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9934616088867188})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8953, 'crossentropy': 0.74525078125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 37048], ['id', 49525], ['id', 29803], ['id', 37974], ['id', 46368]], 'labels': [9, 8, 6, 2, 8], 'scores': [1.1890539068766084, 2.281212485255934, 3.1561360219320242, 3.7855223350099507, 4.1803890565524275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0398385524749756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7983760833740234})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8416097164154053})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8473924398422241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8883028030395508})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0007528066635132})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8340858817100525})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.937573254108429})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9604794979095459})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0115035772323608})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8785, 'crossentropy': 0.8501646484375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 18240], ['id', 50370], ['id', 17558], ['id', 56643], ['id', 34328]], 'labels': [3, 7, 5, 2, 8], 'scores': [1.1548750097368508, 2.1902672614582444, 3.0630730866592675, 3.689338108348185, 4.094430027302139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0738974809646606})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7827510237693787})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7326827049255371})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8122338056564331})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.827411949634552})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8513873815536499})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0027618408203125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.157257080078125})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.83456484375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 7793], ['id', 44672], ['id', 49482], ['id', 5370], ['id', 40434]], 'labels': [8, 2, 1, 3, 5], 'scores': [1.1876366429107077, 2.215768959466013, 3.086232838672771, 3.7000252171656367, 4.096668869105711]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0059814453125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7051835060119629})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6594412326812744})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.837141752243042})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7721798419952393})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6936876773834229})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.599785546875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 20172], ['id', 49354], ['id', 17057], ['id', 21023], ['id', 1239]], 'labels': [4, 0, 4, 2, 8], 'scores': [0.9948242199192363, 1.8781258997520194, 2.6425643345092134, 3.259851178306767, 3.7265804729247805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0823025703430176})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6092181205749512})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6000454425811768})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6540994048118591})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6682140827178955})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7375931143760681})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.584291162109375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 49088], ['id', 17870], ['id', 31624], ['id', 47401], ['id', 4153]], 'labels': [8, 4, 9, 8, 2], 'scores': [1.0229445888853292, 1.9594497590820725, 2.7604608484330573, 3.371568517104051, 3.8122165894603377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9163001775741577})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5302466154098511})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5248215794563293})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49471089243888855})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5095893144607544})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5425877571105957})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5571147203445435})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5697579383850098})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5775081515312195})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5518404245376587})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5313822031021118})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5361395478248596})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.55707939453125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 32880], ['id', 36818], ['id', 13428], ['id', 35401], ['id', 22481]], 'labels': [0, 7, 9, 3, 7], 'scores': [1.208943938806469, 2.2777260279264837, 3.1601774079295053, 3.7744100426824314, 4.15904622840546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0808098316192627})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6033796072006226})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5555078983306885})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.622867226600647})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.571548342704773})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6470760107040405})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.517019921875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 9180], ['id', 39818], ['id', 22550], ['id', 12305], ['id', 46274]], 'labels': [3, 1, 6, 9, 7], 'scores': [0.9883450134338734, 1.8889345709683796, 2.674569475238897, 3.2823087047262174, 3.742042353280307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9856853485107422})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6600809693336487})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5143283605575562})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5719997882843018})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.591277003288269})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6213161945343018})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6171640753746033})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.52918544921875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 9433], ['id', 29320], ['id', 33505], ['id', 42317], ['id', 22269]], 'labels': [7, 1, 2, 5, 2], 'scores': [1.0832437779566226, 2.0494617808450926, 2.8501371434999445, 3.4719514371694835, 3.9015911008196325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0729007720947266})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5924177169799805})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.635676383972168})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5775476098060608})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6626498103141785})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7310690879821777})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6421917676925659})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.531631982421875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 45658], ['id', 47626], ['id', 49658], ['id', 12321], ['id', 47068]], 'labels': [3, -1, 5, 0, 4], 'scores': [1.0179591161280872, 1.9827493154605174, 2.786067392272492, 3.3908947056988206, 3.821853076178037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.075850486755371})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5731646418571472})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5452073216438293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5487764477729797})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5630938410758972})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5943071842193604})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.51476103515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29249], ['id', 11645], ['id', 53873], ['id', 16836], ['id', 37050]], 'labels': [3, 3, 4, 7, 6], 'scores': [0.928529093813582, 1.7821207889379234, 2.535749926121877, 3.140828766585326, 3.605321497499612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0080267190933228})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6078370213508606})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5096796751022339})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47455111145973206})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5321009159088135})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4932020604610443})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.45776767578125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 39429], ['id', 5408], ['id', 27429], ['id', 1674], ['id', 48540]], 'labels': [2, 3, 0, 9, 8], 'scores': [0.9235656476620504, 1.7599410009803549, 2.4664726748856385, 3.0561911641213104, 3.506757703588816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0302183628082275})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5788581967353821})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5448986291885376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5012551546096802})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.56434565782547})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5893360376358032})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5025241374969482})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5225642919540405})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.642214834690094})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.627814531326294})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.48662822265625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 13259], ['id', 52169], ['id', 5303], ['id', 37347], ['id', 6418]], 'labels': [1, 2, 5, 2, 5], 'scores': [1.1182187065476437, 2.1416423582151842, 3.0029545917454854, 3.6344236977653503, 4.04667675333622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.086358666419983})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5447566509246826})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5098404884338379})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5060211420059204})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5017812848091125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5656924843788147})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5666912794113159})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6923830509185791})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.46453583984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 2803], ['id', 5679], ['id', 32561], ['id', 41464], ['id', 59747]], 'labels': [3, 3, 2, 8, 5], 'scores': [1.0607039983124573, 1.963904705041342, 2.7600822819530375, 3.379231272885569, 3.83011077210464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2227731943130493})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6093983054161072})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45047879219055176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5282949209213257})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6654381155967712})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5046733617782593})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5437681078910828})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5479234457015991})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5516735911369324})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.4642607421875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 44570], ['id', 4646], ['id', 18473], ['id', 42787], ['id', 5684]], 'labels': [7, 2, 4, 4, 6], 'scores': [1.0560046009339583, 2.0632390711411395, 2.873209225804789, 3.4931477074038746, 3.9185881469088066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1542998552322388})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6536062955856323})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5399911999702454})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5054398775100708})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47388291358947754})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5584182739257812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6395931243896484})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5799067616462708})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5504639148712158})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.635585367679596})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6426489353179932})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5953730344772339})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.486569482421875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 11572], ['id', 5536], ['id', 46333], ['id', 35643], ['id', 39830]], 'labels': [5, 8, 4, 3, 1], 'scores': [1.1270848970126885, 2.1824496903905253, 3.0331610725697864, 3.681351628074909, 4.099233102684283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3122450113296509})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6573178768157959})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5234308242797852})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5275576114654541})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.575383186340332})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5597158074378967})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5960601568222046})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9393, 'crossentropy': 0.47209560546875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 424], ['id', 37397], ['id', 32776], ['id', 37632], ['id', 2548]], 'labels': [9, 3, 4, 2, 4], 'scores': [1.0097241574013873, 1.9296366563520726, 2.7393540620526498, 3.3600761604475053, 3.8079898787686837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.203462839126587})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5829569697380066})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5414329767227173})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4330557882785797})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47388362884521484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5005043745040894})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47146058082580566})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5240886211395264})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6108618378639221})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5022792816162109})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5546874403953552})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5173718929290771})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5073366761207581})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.558647096157074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5483666658401489})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6001163721084595})
store['active_learning_steps'][33]['training']['best_epoch']=13
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.435478564453125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 43950], ['id', 14062], ['id', 35246], ['id', 670], ['id', 38050]], 'labels': [9, 8, 8, 3, 6], 'scores': [1.2243578407955806, 2.339565574060545, 3.1943910551510992, 3.7937663268789183, 4.168277372780515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2282910346984863})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6488832235336304})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5121014714241028})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5264343023300171})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5177971124649048})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5134504437446594})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.4582849609375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 29132], ['id', 27419], ['id', 26072], ['id', 47278], ['id', 12767]], 'labels': [8, 3, 1, 5, 9], 'scores': [0.878376567349773, 1.6642553886448797, 2.360133773171052, 2.9658369668755737, 3.4252533794473266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.295324444770813})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5715371370315552})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48192813992500305})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4923830032348633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43672239780426025})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44260627031326294})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47074055671691895})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9467, 'crossentropy': 0.43603447265625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 22083], ['id', 10982], ['id', 8093], ['id', 55244], ['id', 38052]], 'labels': [2, 1, 0, 7, 4], 'scores': [1.0446140967222433, 1.9033644881421905, 2.67158395963029, 3.269670001773769, 3.715563571430047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.195253610610962})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5617213249206543})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4686548113822937})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42689311504364014})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44920146465301514})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4445483684539795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5074394941329956})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4766157269477844})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4640918970108032})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.41169638671875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 38275], ['id', 18042], ['id', 42438], ['id', 50930], ['id', 24479]], 'labels': [2, 0, 9, 0, 8], 'scores': [1.111162797689082, 2.097230944198783, 2.900031802121587, 3.5019718471610295, 3.9206485434809926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.308727741241455})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6823052167892456})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5110481381416321})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46335870027542114})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44669997692108154})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4658307135105133})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4246624708175659})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4483223259449005})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42705997824668884})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4712972640991211})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.434701144695282})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.42627734375}
