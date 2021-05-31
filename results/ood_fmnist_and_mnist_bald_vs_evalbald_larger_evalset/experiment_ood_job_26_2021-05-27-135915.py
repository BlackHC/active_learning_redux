store = {}
store['timestamp']=1622120355
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=26']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=26
store['worker_id']=26
store['num_workers']=80
store['config']={'seed': 1261, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2005574703216553})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4250848293304443})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.841845989227295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6365866661071777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 2.0028982421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36122], ['id', 57523], ['id', 39442], ['id', 47651], ['id', 37181]], 'labels': [9, 3, 8, 3, 5], 'scores': [1.2177516974748575, 2.240192573835084, 2.987495651752746, 3.5326811145300683, 3.908696756155212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.97307288646698})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.400585174560547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6200170516967773})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.707446575164795})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6816694736480713})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.1125690937042236})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.6971611976623535})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.716, 'crossentropy': 2.4899001953125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 32022], ['id', 12196], ['id', 33832], ['id', 15753], ['id', 53989]], 'labels': [2, 2, 2, 0, 2], 'scores': [1.277299608917339, 2.371534322058856, 3.2410746789666476, 3.803125005395227, 4.153939287154225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8990757465362549})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.180716037750244})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2012081146240234})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1532468795776367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.674180030822754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.5457029342651367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7146596908569336})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7235, 'crossentropy': 1.9818318359375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 19042], ['id', 14397], ['id', 13460], ['id', 37453], ['id', 46476]], 'labels': [9, 4, 5, 5, 5], 'scores': [1.255846241118891, 2.3014929159060933, 3.1508275651210074, 3.7190547676105776, 4.099250699521102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.0083794593811035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3386430740356445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1738860607147217})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.698302745819092})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5179219245910645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.546091079711914})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.8457703590393066})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.3652310371398926})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7257, 'crossentropy': 2.1401501953125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 7990], ['id', 1589], ['id', 30398], ['id', 27223], ['id', 57305]], 'labels': [6, 7, 3, 2, 1], 'scores': [1.1569819677239148, 2.2051060641645277, 3.059511423345464, 3.676442753945123, 4.0813379176418305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3421272039413452})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4693644046783447})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.638985514640808})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5495233535766602})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9045088291168213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.6441385746002197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.7250571250915527})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8026, 'crossentropy': 1.34217802734375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49438], ['id', 42383], ['id', 22480], ['id', 23877], ['id', 7833]], 'labels': [8, 8, 4, 3, 5], 'scores': [1.1581371560136708, 2.1869967851418206, 3.042439747249283, 3.641605699271855, 4.046507581881526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4170053005218506})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.748004674911499})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.8760746717453003})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.025690793991089})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.0371382236480713})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7869, 'crossentropy': 1.450951171875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 28313], ['id', 42004], ['id', 22083], ['id', 52151], ['id', 27498]], 'labels': [9, 7, 2, 9, 7], 'scores': [1.114766520386024, 2.1211534208895557, 2.901605322203104, 3.4856106695546263, 3.9023023573728866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3726649284362793})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.433567762374878})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7094780206680298})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.61250638961792})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.802262783050537})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8072195053100586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.767961859703064})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.876427173614502})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.9742155075073242})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0806126594543457})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7989, 'crossentropy': 1.5781015625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 39963], ['id', 17755], ['id', 41911], ['id', 50006], ['id', 24716]], 'labels': [4, 0, 2, 5, 5], 'scores': [1.2553521875150775, 2.345878823683197, 3.2308808787400274, 3.830248960701799, 4.189520704768633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6428803205490112})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.941049337387085})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.8976759910583496})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 2.1058249473571777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 2.018918514251709})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.190180540084839})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9584977626800537})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8083, 'crossentropy': 1.65847109375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 39407], ['id', 16860], ['id', 14100], ['id', 50403], ['id', 4646]], 'labels': [0, 8, 5, 3, 2], 'scores': [1.357246277910436, 2.358316270094333, 3.1770451019883996, 3.747530254754757, 4.112252772265446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.271173119544983})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.4045698642730713})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7117173671722412})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.603524923324585})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9131734371185303})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.1794240474700928})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 1.3383517578125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35401], ['id', 42515], ['id', 50858], ['id', 15191], ['id', 7214]], 'labels': [3, 8, 4, 0, 3], 'scores': [1.0517352325150002, 1.9941232857264408, 2.786468281318813, 3.401464380337589, 3.8374619935233625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1897846460342407})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5710300207138062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6002358198165894})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7670495510101318})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.755030870437622})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.637624740600586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.8981772661209106})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.983948826789856})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.8618059158325195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 2.1881399154663086})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.9971723556518555})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 2.049455165863037})
store['active_learning_steps'][9]['training']['best_epoch']=9
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.828, 'crossentropy': 1.5989509765625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 45602], ['id', 24412], ['id', 32323], ['id', 24424], ['id', 40093]], 'labels': [5, 7, 5, 1, 6], 'scores': [1.231204905334875, 2.3599987946908096, 3.2193257171156278, 3.832275002620297, 4.2106855487392245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3028602600097656})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4666309356689453})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6255619525909424})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.4676406383514404})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.6506497859954834})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6941533088684082})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.7648870944976807})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6883896589279175})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8425, 'crossentropy': 1.2907740234375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 57972], ['id', 8691], ['id', 8031], ['id', 14705], ['id', 8516]], 'labels': [4, 2, 8, 0, 7], 'scores': [1.1603390552999946, 2.220755950727372, 3.087722240109411, 3.711386639239123, 4.124203016876041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.05904221534729})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2309449911117554})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.164078950881958})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3132623434066772})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3943700790405273})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.393484354019165})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.46858811378479})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5519273281097412})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 1.082412109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6130], ['id', 4822], ['id', 36078], ['id', 20170], ['id', 23386]], 'labels': [7, 4, 3, 9, 7], 'scores': [1.2351814296109236, 2.3260951546193547, 3.2158481333279187, 3.8275188540341745, 4.212705826236147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0056157112121582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1125510931015015})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1745505332946777})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4298529624938965})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.347869634628296})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3843131065368652})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.95076162109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 59726], ['id', 6604], ['id', 40466], ['id', 21532], ['id', 53504]], 'labels': [5, 8, 8, 5, 2], 'scores': [1.059329312397237, 2.012532595405662, 2.8226451914403166, 3.4538843010628737, 3.8938985942475703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0899757146835327})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2162532806396484})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2562062740325928})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4041757583618164})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3645789623260498})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.5402754545211792})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.7994887828826904})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.4541802406311035})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3886353969573975})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.4237124919891357})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.7771379947662354})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.581050157546997})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.5739619731903076})
store['active_learning_steps'][13]['training']['best_epoch']=10
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8699, 'crossentropy': 1.1955302734375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 13156], ['id', 39822], ['id', 30322], ['ood', 40624], ['id', 49563]], 'labels': [2, 9, 8, -1, 8], 'scores': [1.218454910308217, 2.345566760974029, 3.240958729257521, 3.8469634491121436, 4.20237264116908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1776130199432373})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9732500314712524})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3220243453979492})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3001381158828735})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5159707069396973})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8615, 'crossentropy': 0.85105390625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 7033], ['id', 25384], ['ood', 50403], ['id', 31624], ['id', 57728]], 'labels': [7, 5, -1, 9, 9], 'scores': [1.0070872615625053, 1.9171666008805137, 2.725839801797651, 3.3232363972846146, 3.7780282191194132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2660199403762817})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9880670309066772})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0753636360168457})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1869900226593018})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.234444499015808})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3183188438415527})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8609, 'crossentropy': 0.89585654296875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 17870], ['id', 20322], ['id', 19942], ['id', 57628], ['id', 39830]], 'labels': [4, 1, 5, 2, 1], 'scores': [1.044512664761292, 2.0027137306334586, 2.816639845594361, 3.4305792890349958, 3.867041112091404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1168839931488037})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1739258766174316})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2966761589050293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4548184871673584})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4496119022369385})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6282188892364502})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5648598670959473})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 1.1809642578125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49497], ['id', 43998], ['id', 40775], ['id', 57463], ['id', 32738]], 'labels': [0, 7, 6, 6, 7], 'scores': [1.150414767615053, 2.128261660682404, 2.9458161928352906, 3.548151510204116, 3.9627456459108874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9689502716064453})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9031448364257812})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9134275913238525})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0567500591278076})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0284912586212158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2549439668655396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2521536350250244})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.88122099609375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 12647], ['id', 20832], ['id', 42415], ['id', 34758], ['id', 50320]], 'labels': [1, 2, 7, 8, 5], 'scores': [1.0781111624335074, 2.055776433108588, 2.882882474078624, 3.5195290570968982, 3.9459923619467183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9815176725387573})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9133747816085815})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9636833071708679})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9882373213768005})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0588102340698242})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1455121040344238})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0321242809295654})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.75366552734375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 36744], ['id', 7168], ['id', 14305], ['id', 25960], ['id', 52688]], 'labels': [1, 8, 8, 4, 6], 'scores': [1.0955631086377682, 2.09972832225479, 2.9227807347809875, 3.537652862285105, 3.9540273574415385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0590274333953857})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7474528551101685})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8200230598449707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9730744361877441})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8443397283554077})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9600101709365845})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9076875448226929})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9227131605148315})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.769217138671875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 46530], ['id', 12663], ['id', 15855], ['id', 8821], ['id', 31184]], 'labels': [4, 8, 5, 3, 9], 'scores': [1.1209207330969215, 2.0829282832190774, 2.9228388158083796, 3.559702726334958, 3.991699101878045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.888333797454834})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6975357532501221})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7872083187103271})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7171399593353271})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8203248977661133})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7648234963417053})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.829195499420166})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9819352626800537})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8600404262542725})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.652578515625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 43575], ['id', 17756], ['id', 14317], ['id', 36818], ['id', 20150]], 'labels': [2, 8, 9, 7, 3], 'scores': [1.2190978314387875, 2.2759988630378682, 3.1335060776085157, 3.7420608140511487, 4.118296686677345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9836400151252747})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7143189907073975})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8371031880378723})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8421391844749451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8578834533691406})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9004507064819336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9138557314872742})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8469842672348022})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.6628927734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 5684], ['id', 266], ['id', 24457], ['id', 44898], ['id', 12650]], 'labels': [6, 5, 8, 2, 5], 'scores': [1.0969570434539015, 2.1006133781496623, 2.9551528263590168, 3.6110979080183387, 4.029736493033699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9881412982940674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7821699380874634})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7964092493057251})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7053134441375732})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7754185199737549})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9103338718414307})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8687022924423218})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.639420263671875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5600], ['id', 59314], ['id', 29132], ['id', 49204], ['id', 14655]], 'labels': [6, 9, 8, 9, 3], 'scores': [1.065212506623959, 2.0578694090037373, 2.88015547775601, 3.4961602285910187, 3.9173635686336326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0661711692810059})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6901419162750244})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6554905772209167})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7324983477592468})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6855157017707825})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7103654146194458})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8738196492195129})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8518196940422058})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7571889758110046})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.60179453125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 58560], ['id', 37465], ['id', 59934], ['id', 23422], ['id', 9608]], 'labels': [0, 5, 0, 8, 8], 'scores': [1.1373655668346259, 2.219005194094656, 3.073407985371471, 3.670977826414248, 4.048657571578472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9848646521568298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7145600914955139})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7679619789123535})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6979391574859619})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7251602411270142})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7631843090057373})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8456201553344727})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7429401874542236})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8133671879768372})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7963427305221558})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8657509088516235})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.667060546875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 35864], ['id', 57507], ['id', 8879], ['id', 13752], ['id', 49354]], 'labels': [5, 0, 3, 9, 0], 'scores': [1.1366632986302738, 2.1921778171069795, 3.042775757328261, 3.669453785769587, 4.084986416233667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0250399112701416})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7046130895614624})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6607176661491394})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.685592532157898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7606217861175537})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7077343463897705})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8032519221305847})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8015635013580322})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7912031412124634})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.623339453125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 53693], ['id', 3719], ['id', 28930], ['id', 18487], ['id', 32427]], 'labels': [4, 2, 7, 4, 0], 'scores': [1.1194171529526695, 2.1459220050950227, 2.998545513991684, 3.64226198741214, 4.052228487001101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1795302629470825})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7245945334434509})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6802577972412109})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7022709846496582})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6871012449264526})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7168014645576477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6928061246871948})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8139067888259888})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7977491617202759})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9289859533309937})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.596784033203125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29335], ['id', 26079], ['id', 53872], ['id', 52358], ['id', 5851]], 'labels': [8, 8, 8, 2, 7], 'scores': [1.1861874081411405, 2.1765981433189494, 3.0348876227063135, 3.641029898697969, 4.0347285368270125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1399853229522705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6651284694671631})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6519392728805542})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5596274137496948})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.581760048866272})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6220992803573608})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.714605987071991})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.521271875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 44172], ['id', 40976], ['id', 17540], ['id', 34328], ['id', 52514]], 'labels': [8, 1, 1, 8, 6], 'scores': [0.9771869766054704, 1.8679404215320679, 2.6454970869383665, 3.2844306033627806, 3.749252089850586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1999226808547974})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6074485778808594})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5721544027328491})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5793718099594116})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6022385954856873})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5696326494216919})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.5094546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 39480], ['id', 28512], ['id', 6466], ['id', 26072], ['id', 8214]], 'labels': [9, 5, 2, 1, 7], 'scores': [0.8756526180999078, 1.7019980245863664, 2.4254876080698082, 3.0440169385040656, 3.5366470838503083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2063413858413696})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6510715484619141})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5863189697265625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5613152980804443})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5883985161781311})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6304427981376648})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5944124460220337})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6520569324493408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6283783912658691})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.667863130569458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6278359293937683})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.5741341796875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 9180], ['id', 35652], ['id', 635], ['id', 40654], ['id', 12089]], 'labels': [3, 2, 5, 5, 3], 'scores': [1.2337299140076907, 2.3463304987897136, 3.237249249183484, 3.82282039899618, 4.17183042931263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1846987009048462})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5670516490936279})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5819908380508423})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5229592323303223})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5565974712371826})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5312967300415039})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.557766854763031})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6038739681243896})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5955810546875})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.47552041015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 52099], ['id', 20859], ['id', 17494], ['id', 11292], ['id', 50317]], 'labels': [2, 8, 5, 1, 3], 'scores': [1.1076373153199286, 2.081854449858635, 2.9112665179103585, 3.5469709426752196, 3.985988479143641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2883487939834595})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6672748923301697})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.605707049369812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5470378994941711})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5693085193634033})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5518844723701477})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5494160652160645})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6253905296325684})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.5177482421875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 42703], ['id', 48010], ['id', 35326], ['id', 57474], ['id', 24632]], 'labels': [0, 7, 5, 3, 2], 'scores': [1.148552800668669, 2.0819528430214564, 2.857821201480906, 3.4672644698423847, 3.8911360615991626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1735360622406006})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6945674419403076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5409297347068787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5608614683151245})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5583639144897461})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5484552979469299})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6342174410820007})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.497892578125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 43745], ['id', 52294], ['ood', 50403], ['id', 45944], ['id', 17808]], 'labels': [8, 0, -1, 9, 8], 'scores': [0.9310941888079245, 1.8149204667152858, 2.5806378583706975, 3.20448093158993, 3.671397824206771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.089097499847412})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5990725755691528})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5550327897071838})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5719863772392273})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5727748274803162})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5141672492027283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6469411849975586})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5962109565734863})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5764423608779907})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6460474729537964})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6559290289878845})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6969919204711914})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.509346533203125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 49282], ['id', 424], ['id', 20169], ['id', 36363], ['id', 58832]], 'labels': [2, 9, 4, 6, 3], 'scores': [1.138919654403015, 2.16879083674479, 3.027075471843915, 3.6392221623354466, 4.039567389506719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.158714771270752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5968509912490845})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5468990206718445})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49663597345352173})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5071092844009399})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5687577724456787})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5373939275741577})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49424970149993896})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.458828369140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5013], ['ood', 13195], ['id', 38420], ['id', 29662], ['id', 13942]], 'labels': [2, -1, 8, 2, 4], 'scores': [1.0777951772388472, 1.9884723072886823, 2.789730914194662, 3.4101862364529243, 3.856479365516993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.240835189819336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6256356239318848})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4932306110858917})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6539415121078491})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5365233421325684})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5578967332839966})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.477538916015625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 1674], ['id', 40766], ['id', 37696], ['id', 13922], ['id', 39561]], 'labels': [9, 4, 2, 2, 2], 'scores': [0.8821316272288411, 1.6819462616563556, 2.4204760311879134, 3.0183615327082034, 3.485118652167718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3289625644683838})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6979535818099976})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.561131477355957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6043704748153687})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5796698927879333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6097319722175598})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.52653623046875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 37347], ['id', 41171], ['id', 33812], ['id', 32445], ['id', 31664]], 'labels': [2, 3, 6, 5, 3], 'scores': [0.8920867667908154, 1.678586114539237, 2.399657128354873, 2.9822749860664963, 3.441283613586144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4122521877288818})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6461911201477051})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5605533719062805})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5415504574775696})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5743910670280457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5293421745300293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5350963473320007})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5481533408164978})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5433608293533325})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5659295916557312})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.4759095703125}
