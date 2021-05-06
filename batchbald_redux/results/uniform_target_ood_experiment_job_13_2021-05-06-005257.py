store = {}
store['timestamp']=1620258777
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=13']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=13
store['worker_id']=13
store['num_workers']=40
store['config']={'seed': 16, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1374473571777344})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.434230327606201})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.629298210144043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7301888465881348})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 1.9446859375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 10070], ['id', 30003], ['id', 6398], ['ood', 2473], ['id', 15510], ['id', 14832], ['id', 34436], ['id', 11022], ['id', 14333], ['id', 20482]], 'labels': [9, 9, 3, 8, 2, 7, 2, 0, 3, 0], 'scores': [0.5694249868392944, 1.0185872316360474, 0.7755001783370972, 0.7278695702552795, 1.005998134613037, 1.1325414776802063, 0.7404218912124634, 0.9257454872131348, 0.9238718748092651, 0.8931873440742493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.121843099594116})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.417163372039795})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.7980549335479736})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.0775766372680664})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6555, 'crossentropy': 1.8439763671875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 45344], ['id', 30511], ['id', 17362], ['id', 38986], ['id', 20603], ['id', 24796], ['id', 17931], ['id', 24517], ['id', 54397], ['id', 17505]], 'labels': [5, 3, 8, 3, 6, 2, 4, 2, 3, 1], 'scores': [0.6272121667861938, 0.9152466058731079, 0.680473268032074, 0.6685373783111572, 0.5621324181556702, 0.7506974935531616, 0.5217101573944092, 0.7937604188919067, 0.7707631587982178, 0.6680411100387573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.053406000137329})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4999945163726807})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0903754234313965})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.7554233074188232})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7041, 'crossentropy': 1.8337373046875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43008], ['id', 57236], ['ood', 38223], ['id', 58905], ['id', 34106], ['id', 51171], ['id', 33249], ['ood', 83], ['id', 12257], ['id', 15799]], 'labels': [8, 9, 4, 8, 6, 2, 9, 7, 9, 2], 'scores': [0.9173539876937866, 1.0069247484207153, 0.5491023063659668, 0.6713550090789795, 0.5133459568023682, 0.7769724130630493, 0.7281171083450317, 0.544655442237854, 0.7564688920974731, 0.8358058929443359]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.7368242740631104})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.003352403640747})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.547795534133911})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.6778950691223145})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7093, 'crossentropy': 1.5402619140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 50649], ['id', 37963], ['id', 24107], ['id', 26918], ['id', 46531], ['id', 2605], ['id', 54483], ['id', 51626], ['id', 19430], ['id', 45846]], 'labels': [5, 7, 5, 5, 5, 5, 5, 5, 5, 6], 'scores': [0.8641136288642883, 0.45438623428344727, 0.6911756992340088, 0.73223477602005, 0.6519876718521118, 0.75684654712677, 0.9955705404281616, 0.5822898149490356, 0.6942265033721924, 0.7371150255203247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3358399868011475})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.639455795288086})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8043861389160156})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.8985334634780884})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7751, 'crossentropy': 1.12861884765625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 16216], ['id', 58036], ['id', 17325], ['id', 57324], ['id', 40467], ['id', 45763], ['id', 23169], ['id', 16040], ['id', 31767], ['id', 32607]], 'labels': [4, 0, 4, 8, 8, 2, 5, 8, 9, 8], 'scores': [0.4712669253349304, 0.506320595741272, 0.5367653369903564, 0.556245744228363, 0.7653384208679199, 0.7003055810928345, 0.6470558643341064, 0.5189965963363647, 0.4081214666366577, 0.6503372192382812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0709729194641113})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1944191455841064})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2398085594177246})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3744293451309204})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8138, 'crossentropy': 0.9197947265625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 22648], ['id', 12803], ['id', 29899], ['id', 25120], ['id', 55685], ['id', 51988], ['id', 11441], ['id', 2715], ['id', 54469], ['id', 59170]], 'labels': [9, 2, 3, 8, 5, 7, 3, 4, 8, 5], 'scores': [0.5941874980926514, 0.620064377784729, 0.6731940507888794, 0.4934622645378113, 0.5132715702056885, 0.5790486335754395, 0.3880193829536438, 0.33091259002685547, 0.5429966449737549, 0.5710799098014832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1464080810546875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1934001445770264})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3574538230895996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4064449071884155})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8092, 'crossentropy': 0.99582734375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 40398], ['id', 29289], ['id', 39558], ['id', 36491], ['id', 47757], ['id', 39573], ['id', 12347], ['id', 2145], ['id', 21013], ['id', 48927]], 'labels': [8, 3, 4, 6, 5, 5, 5, 7, 5, 9], 'scores': [0.4956338405609131, 0.571972519159317, 0.5235439538955688, 0.6873593330383301, 0.4277493953704834, 0.758912205696106, 0.41483473777770996, 0.5524498820304871, 0.5590949058532715, 0.40672624111175537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8867505788803101})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8877788782119751})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0482628345489502})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0647084712982178})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8611, 'crossentropy': 0.783191748046875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22083], ['id', 18390], ['id', 9403], ['ood', 56203], ['id', 10242], ['id', 36337], ['id', 36066], ['id', 34422], ['id', 55603], ['id', 33763]], 'labels': [2, 3, 3, 7, 0, 3, 8, 8, 7, 3], 'scores': [0.6312069892883301, 0.5887273550033569, 0.542158305644989, 0.3887174129486084, 0.42955631017684937, 0.6743620038032532, 0.4232674241065979, 0.5668823719024658, 0.4904441237449646, 0.3689475655555725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8349705934524536})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7604609727859497})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8542397022247314})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8504983186721802})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9177152514457703})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8922, 'crossentropy': 0.64665771484375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23916], ['id', 40378], ['id', 22573], ['id', 16473], ['id', 57982], ['id', 5038], ['id', 37555], ['id', 42037], ['id', 18413], ['id', 32668]], 'labels': [2, 7, 2, 2, 5, 4, 3, 2, 2, 9], 'scores': [0.6003257632255554, 0.6654798090457916, 0.668176144361496, 0.9147661030292511, 0.6897289156913757, 0.5769565105438232, 0.7052305936813354, 0.6795002818107605, 0.7307509183883667, 0.6616419553756714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9338533878326416})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7546354532241821})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.834833025932312})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.844551682472229})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9056731462478638})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.586411376953125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 44096], ['id', 51986], ['id', 10012], ['id', 37838], ['id', 32702], ['id', 44234], ['id', 59779], ['id', 1149], ['id', 12355], ['id', 55513]], 'labels': [0, 2, 8, 2, 5, 9, 7, 4, 3, 5], 'scores': [0.4618823826313019, 0.839148998260498, 0.562380313873291, 0.6666457653045654, 0.6684999465942383, 0.8823378682136536, 0.8727329969406128, 0.625281572341919, 0.5405985116958618, 0.9226703643798828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8245924115180969})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7015458345413208})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7736341953277588})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7108638286590576})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7891459465026855})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.59724541015625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 32519], ['id', 33957], ['id', 57303], ['id', 19886], ['id', 5013], ['id', 7951], ['id', 24992], ['id', 4955], ['id', 20068], ['id', 49893]], 'labels': [5, 7, 1, 2, 2, 1, 4, 2, 8, 3], 'scores': [0.8961072564125061, 0.3111092448234558, 0.6707849502563477, 0.701452910900116, 0.9665820002555847, 0.6071799993515015, 0.7148553729057312, 0.9873179793357849, 0.5167644619941711, 0.7288795113563538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8806450963020325})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6971496343612671})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7001453638076782})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7723146677017212})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7300616502761841})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9005, 'crossentropy': 0.5866810546875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 7437], ['id', 57686], ['id', 42833], ['id', 31625], ['id', 43548], ['id', 10925], ['id', 21012], ['id', 18487], ['id', 52460], ['id', 24263]], 'labels': [7, 0, 8, 0, 8, 6, 2, 4, 7, 9], 'scores': [0.6710084080696106, 0.45586514472961426, 0.6504765748977661, 0.5205402374267578, 0.5598552823066711, 0.6525133848190308, 0.6759921312332153, 0.5831897258758545, 0.6450313329696655, 0.6153450012207031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9659585952758789})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6606117486953735})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5539847612380981})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6581568717956543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5987225770950317})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6374229192733765})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.50023408203125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 38640], ['id', 5649], ['id', 29528], ['id', 15390], ['id', 8865], ['id', 40208], ['id', 15450], ['id', 22211], ['id', 55396], ['id', 44270]], 'labels': [6, 3, 3, 5, 3, 0, 6, 5, 5, 8], 'scores': [0.6888847649097443, 0.7417115569114685, 0.512693464756012, 0.44153153896331787, 0.4866166114807129, 0.7971547245979309, 0.5432290434837341, 0.7290131449699402, 0.6756066083908081, 0.6149871349334717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9928492307662964})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6880026459693909})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5737041234970093})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6136003732681274})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.578165590763092})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7088080644607544})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.517136767578125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37439], ['id', 56288], ['id', 25008], ['id', 6137], ['id', 45024], ['id', 33956], ['id', 20869], ['id', 3762], ['ood', 47743], ['ood', 54482]], 'labels': [3, 3, 8, 0, 5, 8, 3, 8, 3, 5], 'scores': [0.7151179313659668, 0.6082112789154053, 0.8205583691596985, 0.6561430394649506, 0.8025278449058533, 0.759011447429657, 0.7760327458381653, 0.8861224055290222, 0.6762704849243164, 0.6358395218849182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9257350564002991})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6303248405456543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5887508392333984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5322059392929077})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.542391300201416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5498479008674622})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4959002733230591})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.544400691986084})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5835869908332825})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5573133826255798})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.460916357421875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 53854], ['id', 27984], ['id', 45770], ['id', 33748], ['id', 47828], ['id', 41328], ['id', 32532], ['id', 39031], ['id', 13639], ['id', 39728]], 'labels': [8, 7, 5, 5, 5, 7, 9, 2, 8, 3], 'scores': [0.7978292107582092, 0.7857699394226074, 0.8432011008262634, 0.8234084844589233, 0.781726598739624, 0.5727968811988831, 0.5788204669952393, 0.6995258331298828, 0.626742422580719, 0.5792195200920105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.929287314414978})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5528026223182678})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49381223320961})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5234057903289795})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5005297660827637})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5186079144477844})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.4048334716796875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48546], ['id', 50445], ['id', 58811], ['id', 13995], ['id', 40046], ['id', 33812], ['id', 5830], ['id', 20013], ['id', 46447], ['id', 47322]], 'labels': [4, 9, 2, 6, 7, 6, 0, 6, 2, 8], 'scores': [0.6925630569458008, 0.733805239200592, 0.6708780527114868, 0.4467827081680298, 0.7583099603652954, 0.9429693818092346, 0.49889129400253296, 0.4380243718624115, 0.6457191705703735, 0.5880588889122009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9186341166496277})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5659720301628113})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5003013014793396})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46232888102531433})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5091162919998169})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5005353093147278})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.563965380191803})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9447, 'crossentropy': 0.3747544677734375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 26460], ['id', 23314], ['id', 17585], ['id', 54104], ['id', 47140], ['id', 25246], ['id', 56412], ['id', 27337], ['id', 28530], ['id', 38332]], 'labels': [5, 9, 0, 0, 3, 2, 8, 5, 9, 0], 'scores': [0.48537296056747437, 0.4587377905845642, 0.7329218983650208, 0.7759011387825012, 0.8206978440284729, 0.7614303529262543, 0.5576189756393433, 0.5798793733119965, 0.44677555561065674, 0.409392848610878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9403424263000488})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5153108835220337})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44394901394844055})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4530675709247589})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44445592164993286})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5055865049362183})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9467, 'crossentropy': 0.3799479736328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 38319], ['id', 14821], ['id', 39865], ['id', 48102], ['id', 51856], ['id', 39305], ['id', 56324], ['id', 41489], ['id', 31301], ['id', 1676]], 'labels': [2, 1, 8, 7, 7, 7, 3, 2, 5, 1], 'scores': [0.7918524742126465, 0.7777552604675293, 0.5298434495925903, 0.890668511390686, 0.7489303946495056, 0.7787445783615112, 0.47140055894851685, 0.6684561967849731, 0.7793588638305664, 0.7220145463943481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0037282705307007})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5660198330879211})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5036886930465698})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4351350665092468})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46688634157180786})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43189090490341187})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46103474497795105})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41236066818237305})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4520304799079895})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4871166944503784})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.472525030374527})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.3694575439453125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 3765], ['id', 34458], ['id', 2352], ['id', 28512], ['id', 17958], ['ood', 59590], ['id', 50320], ['id', 10021], ['id', 30883], ['id', 46521]], 'labels': [2, 9, 0, 5, 9, 0, 5, 8, 3, 6], 'scores': [0.6790735721588135, 0.5097147822380066, 0.8358627557754517, 0.7849111557006836, 1.1182183027267456, 0.6296379566192627, 0.7348325252532959, 0.6257146000862122, 0.7704424858093262, 0.5739616751670837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9083483219146729})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5047098994255066})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41916197538375854})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43479400873184204})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3846363425254822})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4172244071960449})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38583874702453613})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42706865072250366})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.3257702880859375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 43660], ['id', 55438], ['id', 14072], ['id', 37885], ['id', 4058], ['id', 57378], ['id', 25847], ['id', 27150], ['id', 47946], ['id', 42199]], 'labels': [9, 8, 6, 8, 8, 1, 1, 2, 3, 3], 'scores': [0.7549797892570496, 1.0118345618247986, 0.6350458860397339, 0.7389876842498779, 0.9267769455909729, 0.41823810338974, 0.6136868000030518, 0.5448671281337738, 0.8244971036911011, 0.7131673097610474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9267827868461609})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5230058431625366})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4611419141292572})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3917413651943207})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40751510858535767})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43548813462257385})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4522508382797241})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9476, 'crossentropy': 0.353408984375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 132], ['id', 42687], ['id', 49332], ['id', 13538], ['id', 36744], ['id', 2622], ['id', 19106], ['id', 27952], ['id', 51544], ['id', 31307]], 'labels': [5, 5, 8, 5, 1, 5, 5, 5, 1, 1], 'scores': [0.5822601318359375, 0.8742832541465759, 0.3411805331707001, 0.8519062399864197, 0.9844531416893005, 0.7300455570220947, 0.5274590849876404, 0.9154568314552307, 0.8306806087493896, 0.6306729316711426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9261246919631958})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.541766881942749})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.416067898273468})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4052202105522156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43843749165534973})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4221276640892029})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3952314853668213})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.401119202375412})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45890235900878906})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41423293948173523})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9531, 'crossentropy': 0.331383837890625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 29676], ['id', 1812], ['id', 34414], ['id', 33198], ['id', 4638], ['id', 38372], ['id', 43125], ['id', 50605], ['id', 2250], ['id', 47100]], 'labels': [5, 4, 8, 8, 3, 4, 6, 7, 5, 8], 'scores': [0.721764087677002, 0.8741152882575989, 0.8171149492263794, 0.6259984970092773, 0.8568465709686279, 0.3724438548088074, 0.6223542094230652, 0.7224625051021576, 0.7641095519065857, 0.6856403946876526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9277451038360596})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5203803777694702})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3710952401161194})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3574787974357605})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3688865900039673})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3853492736816406})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34930843114852905})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36988896131515503})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38608574867248535})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3568604290485382})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9525, 'crossentropy': 0.3330896484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 38760], ['id', 55856], ['id', 21040], ['id', 44624], ['ood', 4194], ['id', 49957], ['id', 39316], ['id', 12663], ['id', 51502], ['id', 43034]], 'labels': [9, 9, 9, 8, 5, 5, 7, 8, 7, 9], 'scores': [0.9629066586494446, 0.5059752464294434, 1.0455965399742126, 0.5921456813812256, 0.552910327911377, 0.41323423385620117, 0.7130177021026611, 0.8966104984283447, 0.6054258942604065, 0.5417575836181641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0797615051269531})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5739847421646118})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4941233694553375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44571053981781006})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4827880263328552})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4121917486190796})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41303718090057373})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3993222713470459})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4367086589336395})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4577535390853882})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46752625703811646})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3381636474609375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 54520], ['id', 53570], ['id', 29286], ['id', 24491], ['ood', 27427], ['id', 57882], ['id', 53044], ['id', 12768], ['id', 14540], ['id', 13774]], 'labels': [9, 3, 9, 2, 4, 0, 9, 9, 7, 2], 'scores': [0.8293092250823975, 0.8502194881439209, 0.7277061939239502, 0.7074819803237915, 0.4552537202835083, 0.9100087881088257, 0.8982650637626648, 0.8010629415512085, 0.7100543975830078, 0.5048295259475708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0685631036758423})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5369352102279663})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46505123376846313})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4126625955104828})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39505448937416077})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38471055030822754})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42729341983795166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3946024179458618})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38750165700912476})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.329081201171875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 48156], ['id', 6430], ['id', 27576], ['id', 939], ['id', 50414], ['id', 38920], ['id', 38974], ['id', 33162], ['id', 26850], ['id', 11784]], 'labels': [6, 3, 5, 6, 9, 7, 1, 8, 2, 6], 'scores': [0.7370210289955139, 0.7647359371185303, 0.8414419293403625, 0.40791451930999756, 0.781654417514801, 0.7968896627426147, 0.720018744468689, 0.9071605205535889, 0.8156896233558655, 0.6807944178581238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0106390714645386})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5663449168205261})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41188180446624756})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3768884539604187})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4032015800476074})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37263786792755127})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36886066198349})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39770546555519104})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3834952116012573})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37101107835769653})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9539, 'crossentropy': 0.335937890625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 43393], ['id', 42472], ['id', 17679], ['id', 50461], ['id', 28617], ['id', 470], ['id', 53300], ['id', 11322], ['id', 5295], ['id', 38001]], 'labels': [3, 2, 8, 7, 5, 1, 4, 8, 4, 7], 'scores': [0.4603897035121918, 0.8544824123382568, 0.731759786605835, 0.6785402894020081, 0.642583966255188, 0.9096730351448059, 0.5883964598178864, 0.436892032623291, 0.9095865488052368, 0.7675707042217255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9425661563873291})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5171994566917419})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38426828384399414})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33088916540145874})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3422348201274872})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31288108229637146})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.327509343624115})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34344714879989624})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3043076694011688})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32476627826690674})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3394061326980591})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3190610408782959})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9633, 'crossentropy': 0.29127626953125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 31917], ['id', 6466], ['ood', 27436], ['id', 26600], ['id', 42415], ['id', 46025], ['id', 16755], ['id', 52729], ['id', 41371], ['id', 47690]], 'labels': [9, 2, 1, 7, 7, 8, 3, 4, 0, 0], 'scores': [0.7970351874828339, 0.8453160524368286, 0.5411868095397949, 0.6686388850212097, 0.9790210127830505, 0.6434969902038574, 0.7458353042602539, 0.6782707571983337, 0.6370219588279724, 0.733555793762207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.067441463470459})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.47919005155563354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3662121891975403})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33040890097618103})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3235465884208679})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32253018021583557})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34641486406326294})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32828477025032043})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31877100467681885})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3211324214935303})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3412958085536957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3561493158340454})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.29057255859375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 7741], ['id', 23358], ['id', 6459], ['id', 26358], ['id', 31652], ['id', 39942], ['id', 2765], ['id', 15723], ['id', 52899], ['id', 12196]], 'labels': [6, 6, 9, 3, 9, 9, 0, 8, 7, 2], 'scores': [0.6505781412124634, 0.6409079134464264, 0.6964883208274841, 0.7864924073219299, 0.6714159846305847, 0.8478716611862183, 0.7648946046829224, 0.7574247121810913, 0.5823515355587006, 0.656417965888977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9944997429847717})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5989494323730469})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3567507266998291})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3846539556980133})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3581290543079376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3343808650970459})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35003191232681274})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34169331192970276})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3741600811481476})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.30791669921875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 45114], ['id', 50431], ['id', 12938], ['id', 9455], ['id', 21426], ['id', 17365], ['id', 34378], ['id', 27291], ['id', 45339], ['id', 52456]], 'labels': [7, 3, 2, 0, 6, 0, 7, 5, 4, 2], 'scores': [0.49273014068603516, 0.6693028211593628, 0.5785195827484131, 0.356867253780365, 0.8149062991142273, 0.7501078844070435, 0.599544882774353, 0.5024169981479645, 0.4304982125759125, 0.5700546503067017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9739242792129517})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49255430698394775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.378299355506897})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3491567373275757})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3194109797477722})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3134801387786865})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3259313404560089})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3649389147758484})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35485872626304626})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.2906095703125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 14305], ['id', 44736], ['id', 50827], ['id', 29444], ['id', 34402], ['id', 5740], ['id', 45381], ['id', 22442], ['id', 38626], ['id', 48880]], 'labels': [8, 5, 1, 4, 1, 9, 9, 2, 5, 4], 'scores': [0.8537880778312683, 0.7616997063159943, 0.7211202383041382, 0.7080479860305786, 0.625621885061264, 0.9253518581390381, 0.639127790927887, 0.569256454706192, 0.9182083010673523, 0.6772969365119934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0609078407287598})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5305236577987671})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4176282286643982})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33151715993881226})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2938607931137085})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32017719745635986})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33928951621055603})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3300449550151825})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.27840029296875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 49088], ['id', 37347], ['id', 30968], ['id', 41612], ['id', 37688], ['id', 41299], ['id', 16678], ['id', 35694], ['id', 37048], ['id', 57751]], 'labels': [8, 2, 6, 0, 9, 3, 3, 9, 9, 7], 'scores': [0.7050872445106506, 0.7555553317070007, 0.5216440558433533, 0.29999178647994995, 0.5825705528259277, 0.5359929800033569, 0.7428698539733887, 0.6106647253036499, 0.8466291427612305, 0.4667791724205017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.990240216255188})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.45349469780921936})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39823412895202637})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3405390977859497})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.321775883436203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35796409845352173})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33692002296447754})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32077258825302124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3179929256439209})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38153278827667236})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4000621438026428})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35061314702033997})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.320512841796875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 54880], ['id', 47475], ['id', 59747], ['id', 24589], ['id', 9384], ['id', 29872], ['id', 10446], ['id', 40259], ['id', 58560], ['id', 10555]], 'labels': [5, 5, 5, 8, 5, 6, 8, 8, 0, 1], 'scores': [0.6242440640926361, 0.8210110664367676, 0.9264925718307495, 0.9749494194984436, 0.8717281222343445, 0.6433185935020447, 0.7963771224021912, 0.8788554668426514, 0.8471702039241791, 0.6912474632263184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1870636940002441})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5811187028884888})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41888612508773804})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31823620200157166})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3014844059944153})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34881091117858887})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31330162286758423})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32604390382766724})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.2873529541015625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 37016], ['id', 35962], ['id', 31068], ['id', 51131], ['id', 11645], ['id', 20650], ['id', 59339], ['id', 36427], ['id', 54798], ['id', 58388]], 'labels': [5, 6, 2, 2, 3, 4, 1, 3, 3, 2], 'scores': [0.4096757471561432, 0.624683678150177, 0.692463755607605, 0.5210453271865845, 0.6169048547744751, 0.607627809047699, 0.633176326751709, 0.5178635716438293, 0.6483920216560364, 0.3659183382987976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1649436950683594})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.48069119453430176})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4039655923843384})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3273801803588867})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3402060270309448})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30746933817863464})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30941203236579895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31816068291664124})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3015022277832031})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34864532947540283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3309069275856018})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3532714247703552})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.265705224609375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 50576], ['id', 27453], ['id', 40517], ['id', 27167], ['id', 14062], ['id', 55496], ['id', 9717], ['id', 19124], ['id', 31738], ['id', 42139]], 'labels': [2, 7, 3, 3, 8, 9, 0, 8, 8, 4], 'scores': [0.7910844683647156, 0.7104485929012299, 0.6526339054107666, 0.4621681272983551, 0.7971312999725342, 0.9607937932014465, 0.7808670997619629, 0.5151180624961853, 0.8301321864128113, 0.7773631811141968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0070499181747437})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.569515585899353})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4162474274635315})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3888055086135864})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31179848313331604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3040575683116913})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.329356849193573})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3354092836380005})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3527621328830719})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2755932861328125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 54858], ['id', 9727], ['id', 32346], ['id', 46368], ['id', 27172], ['id', 44927], ['id', 41378], ['id', 44670], ['id', 7308], ['id', 22522]], 'labels': [3, 2, 7, 8, 3, 7, 3, 9, 8, 3], 'scores': [0.6942305564880371, 0.34600597620010376, 0.6662629842758179, 0.9539974927902222, 0.6388440728187561, 0.6878631711006165, 0.521179586648941, 0.49227404594421387, 0.6786448955535889, 0.7006465196609497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.989823579788208})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5526301264762878})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3495258688926697})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32008904218673706})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30289024114608765})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29404544830322266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34720009565353394})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30051499605178833})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32188117504119873})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.243648876953125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 10800], ['id', 5632], ['id', 37794], ['id', 20169], ['ood', 30363], ['id', 19981], ['id', 47723], ['ood', 29104], ['id', 17941], ['id', 53873]], 'labels': [8, 6, 4, 4, 9, 8, 8, 7, 0, 4], 'scores': [0.5765078663825989, 0.5882721245288849, 0.5945048332214355, 0.795506477355957, 0.39642202854156494, 0.8015553951263428, 0.5562596917152405, 0.3351837396621704, 0.8203231692314148, 0.8846875429153442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1810060739517212})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6428240537643433})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4264947772026062})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35268840193748474})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3332277238368988})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30877217650413513})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3165399432182312})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3198695778846741})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3069937825202942})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3328689932823181})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32886648178100586})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3288751244544983})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.273384814453125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 20170], ['id', 22102], ['id', 13127], ['id', 3136], ['ood', 31223], ['id', 602], ['ood', 38912], ['id', 28149], ['id', 43248], ['id', 44961]], 'labels': [9, 5, 3, 6, 5, 8, 5, 9, 9, 8], 'scores': [0.8919689059257507, 0.6151063740253448, 0.7250784635543823, 0.7751248478889465, 0.29779744148254395, 0.7195718884468079, 0.6455323696136475, 0.7690376937389374, 0.7392677068710327, 0.8455463647842407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0260581970214844})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6136883497238159})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3630117177963257})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32346126437187195})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.288453072309494})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2791324853897095})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30133986473083496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29482418298721313})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26641035079956055})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3039320707321167})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2873348891735077})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30381590127944946})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2426296630859375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 56066], ['id', 13153], ['id', 5679], ['id', 17466], ['id', 40236], ['id', 40076], ['id', 10048], ['id', 28154], ['id', 52326], ['id', 22976]], 'labels': [7, 9, 3, 0, 4, 2, 1, 2, 5, 8], 'scores': [0.8279557824134827, 0.6570465266704559, 0.7124376893043518, 0.606052041053772, 0.6658701300621033, 0.5879184007644653, 0.7304301261901855, 0.5081193447113037, 0.37990427017211914, 0.492834210395813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2430319786071777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5537756681442261})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3816966414451599})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3290475606918335})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2741393744945526})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2697809338569641})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2841551899909973})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25846606492996216})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27630865573883057})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2678492069244385})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26497721672058105})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.23551123046875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 39673], ['id', 9774], ['id', 45056], ['id', 26444], ['id', 50369], ['id', 5774], ['id', 50090], ['id', 36765], ['id', 17091], ['id', 34740]], 'labels': [2, 7, 8, 1, 3, 6, 4, 1, 4, 3], 'scores': [0.5904711484909058, 0.5014011859893799, 0.6479926109313965, 0.5824605226516724, 0.6458434462547302, 0.6116727590560913, 0.6738567352294922, 0.5168269872665405, 0.5549677014350891, 0.7199615240097046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2413016557693481})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5742272138595581})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4202116131782532})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3231191039085388})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27542850375175476})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27835652232170105})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2908098101615906})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2581527829170227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2814924716949463})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27769121527671814})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27837705612182617})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.25638388671875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 41295], ['id', 27358], ['id', 27685], ['id', 5065], ['id', 14546], ['id', 50346], ['id', 57956], ['id', 45602], ['id', 503], ['id', 8721]], 'labels': [9, 8, 6, 2, 4, 8, 2, 5, 8, 9], 'scores': [0.8523945808410645, 0.7586230039596558, 0.6351405382156372, 0.4127357006072998, 0.6915865540504456, 0.6533218026161194, 0.7364823818206787, 0.6155480742454529, 0.5171095728874207, 0.6896739602088928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0979499816894531})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6200922727584839})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38039451837539673})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3301006853580475})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29272177815437317})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3119460344314575})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2835463583469391})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32225120067596436})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29994016885757446})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3341919183731079})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.2702858642578125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 24492], ['id', 54937], ['id', 7270], ['id', 27464], ['id', 12493], ['id', 7229], ['id', 22364], ['id', 36314], ['id', 49517], ['id', 46734]], 'labels': [5, 7, 5, 2, 8, 7, 0, 4, 6, 4], 'scores': [0.46463167667388916, 0.6722822189331055, 0.7141896486282349, 0.617890477180481, 0.5004644393920898, 0.7588683366775513, 0.6439031362533569, 0.48869985342025757, 0.7804168462753296, 0.5944483280181885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.052848219871521})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5847482681274414})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39664360880851746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30408596992492676})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2778995633125305})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27793043851852417})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28759217262268066})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25801658630371094})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2924792766571045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2681030035018921})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29533886909484863})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2355556640625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 34406], ['id', 137], ['id', 50417], ['ood', 17248], ['id', 49163], ['id', 38698], ['id', 5842], ['id', 50572], ['id', 39389], ['id', 59401]], 'labels': [4, 8, 3, 5, 9, 5, 1, 1, 8, 4], 'scores': [0.7152040004730225, 0.5771466493606567, 0.7066610455513, 0.5222755670547485, 0.6254571080207825, 0.8895619511604309, 0.6009887158870697, 0.5699138641357422, 0.6733068823814392, 0.5962603688240051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.292311191558838})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6448426246643066})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40242326259613037})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3374685049057007})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3879457116127014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29330354928970337})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32369837164878845})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28518468141555786})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.291034460067749})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29563120007514954})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30413633584976196})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.2657741455078125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 40050], ['id', 17040], ['id', 2728], ['id', 424], ['id', 25310], ['id', 15771], ['id', 39208], ['id', 48154], ['id', 18302], ['id', 38969]], 'labels': [9, 3, 9, 9, 1, 5, 5, 9, 6, 9], 'scores': [0.7006011009216309, 0.6531269550323486, 0.6874716281890869, 0.8040237426757812, 0.6116942167282104, 0.4115903377532959, 0.7965824007987976, 0.7574033737182617, 0.5570363402366638, 0.8185510039329529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1029412746429443})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5337396860122681})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34685781598091125})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3213909864425659})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2952413558959961})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2884051501750946})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28406086564064026})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2547791004180908})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2310948669910431})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2817934453487396})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26940470933914185})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2806030511856079})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.227198291015625}
